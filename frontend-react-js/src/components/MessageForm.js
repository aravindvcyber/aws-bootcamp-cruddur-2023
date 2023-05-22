import './MessageForm.css';
import React from "react";
import process from 'process';
import { useParams } from 'react-router-dom';
import {post} from 'lib/Requests';
import FormErrors from 'components/FormErrors';

export default function ActivityForm(props) {
  const [count, setCount] = React.useState(0);
  const [message, setMessage] = React.useState('');
  const [errors, setErrors] = React.useState('');
  const params = useParams();

  const classes = []
  classes.push('count')
  if (1024-count < 0){
    classes.push('err')
  }

  const onsubmit = async (event) => {
    event.preventDefault();
    // try {
    //   const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/messages`
    //   console.log('onsubmit payload', message)
    //   let json = { 'message': message }
    //   if (params.handle) {
    //     json.handle = params.handle
    //   } else {
    //     json.message_group_uuid = params.message_group_uuid
    //   }
    //   await getAccessToken()
    //   const access_token = localStorage.getItem("access_token")
    //   const res = await fetch(backend_url, {
    //     method: "POST",
    //     headers: {
    //       // 'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
    //       'Authorization': `Bearer ${access_token}`,
    //       'Accept': 'application/json',
    //       'Content-Type': 'application/json'
    //     },
    //     // body: JSON.stringify({
    //     //   message: message,
    //     //   user_receiver_handle: params.handle
    //     // }),
    //     body: JSON.stringify(json)
    //   });
    //   let data = await res.json();
    //   if (res.status === 200) {
    //     // props.setMessages(current => [...current,data]);
    //     console.log('data:',data)
    //     if (data.message_group_uuid) {
    //       console.log('redirect to message group')
    //       window.location.href = `/messages/${data.message_group_uuid}`
    //     } else {
    //       props.setMessages(current => [...current,data]);
    //     }
    //   } else {
    //     console.log(res)
    //   }
    const url = `${process.env.REACT_APP_BACKEND_URL}/api/messages`
    let payload_data = { 'message': message }
    if (params.handle) {
      payload_data.handle = params.handle
    } else {
      payload_data.message_group_uuid = params.message_group_uuid
    }
    post(url,payload_data,{
      auth: true,
      setErrors: setErrors,
      success: function(){
        console.log('data:',payload_data)
        if (payload_data.message_group_uuid) {
          console.log('redirect to message group')
          window.location.href = `/messages/${payload_data.message_group_uuid}`
        } else {
          props.setMessages(current => [...current,payload_data]);
        }
      }
    // } catch (err) {
    //   console.log(err);
    // }
  })
  }

  const textarea_onchange = (event) => {
    setCount(event.target.value.length);
    setMessage(event.target.value);
  }

  return (
    <form 
      className='message_form'
      onSubmit={onsubmit}
    >
      <textarea
        type="text"
        placeholder="send a direct message..."
        value={message}
        onChange={textarea_onchange} 
      />
      <div className='submit'>
        <div className={classes.join(' ')}>{1024-count}</div>
        <button type='submit'>Message</button>
      </div>
      <FormErrors errors={errors} />
    </form>
  );
}