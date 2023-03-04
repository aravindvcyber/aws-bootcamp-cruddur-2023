// tracing.js
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { WebTracerProvider, BatchSpanProcessor } from '@opentelemetry/sdk-trace-web';
import { ZoneContextManager } from '@opentelemetry/context-zone';
import { Resource } from '@opentelemetry/resources';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';
import { XMLHttpRequestInstrumentation } from '@opentelemetry/instrumentation-xml-http-request';
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch';


import { UserInteractionInstrumentation } from '@opentelemetry/instrumentation-user-interaction';
import { registerInstrumentations } from '@opentelemetry/instrumentation';



const exporter = new OTLPTraceExporter({
     //url: 'https://<your collector endpoint>:443/v1/traces'
     url: "https://api.honeycomb.io/v1/traces",
     headers: {
          // client side browser 
          "x-honeycomb-team": "4sfRS5VpEKO8SnAtMH4LRF",
     },
});
const provider = new WebTracerProvider({
     resource: new Resource({
          [SemanticResourceAttributes.SERVICE_NAME]: 'crudder-frontend-react',
     }),
});
provider.addSpanProcessor(new BatchSpanProcessor(exporter));
provider.register({
     contextManager: new ZoneContextManager()
});

// add auto-instrumentation
registerInstrumentations({
     instrumentations: [
          new XMLHttpRequestInstrumentation({
               propagateTraceHeaderCorsUrls: [
                    /.+/g, //Regex to match your backend urls. This should be updated.
               ]
          }),
          new FetchInstrumentation({
               propagateTraceHeaderCorsUrls: [
                    /.+/g, //Regex to match your backend urls. This should be updated.
               ]
          }),
     ],
});

registerInstrumentations({
  instrumentations: [
    new UserInteractionInstrumentation({
      eventNames: ['submit', 'click', 'keypress'],
      shouldPreventSpanCreation: (event, element, span) => {
        span.setAttribute('target.id', element.id)
      }
    }),
  ],
});