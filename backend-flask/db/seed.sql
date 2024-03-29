-- this file was manually created

INSERT INTO public.users (display_name, handle, email,cognito_user_id)
VALUES
  ('Aravind Vadamalaimuthu', 'aravindvcyber' ,'aravindvcyber@gmail.com','92da1eb4-1688-4d72-9de4-b73f8dafda88'),
  ('Alt Brown','altbrown', 'andrew@cloudprojectbootcamp.com' ,'MOCK'),
  ('Andrew Brown', 'andrewbrown' ,'andrewbrown@example.com','MOCK'),
  ('Andrew Bayko', 'bayko' ,'bayko@example.com','MOCK');

-- delete from public.users where handle = 'aravindvcyber';

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  );


INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'aravindvcyber' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '3 day'
  );

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'bayko' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '20 day'
  );