import './MessageGroupPage.css';
import React from "react";
import { useParams } from 'react-router-dom';

// import {checkAuth, getAccessToken} from '../lib/CheckAuth';
// import DesktopNavigation  from '../components/DesktopNavigation';
// import MessageGroupFeed from '../components/MessageGroupFeed';
// import MessagesFeed from '../components/MessageFeed';
// import MessagesForm from '../components/MessageForm';

import {get} from 'lib/Requests';
import {checkAuth} from 'lib/CheckAuth';

import DesktopNavigation  from 'components/DesktopNavigation';
import MessageGroupFeed from 'components/MessageGroupFeed';
import MessagesFeed from 'components/MessageFeed';
import MessagesForm from 'components/MessageForm';

// [TODO] Authenication
//import Cookies from 'js-cookie'

export default function MessageGroupPage() {
  const [messageGroups, setMessageGroups] = React.useState([]);
  const [messages, setMessages] = React.useState([]);
  const [popped, setPopped] = React.useState([]);
  const [user, setUser] = React.useState(null);
  const dataFetchedRef = React.useRef(false);
  const params = useParams();

  const loadMessageGroupsData = async () => {
  //   try {
  //     const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/message_groups`
  //     await getAccessToken()
  //     const access_token = localStorage.getItem("access_token")
  //     const res = await fetch(backend_url, {
  //       headers: {
  //         Authorization: `Bearer ${access_token}`
  //       },
  //       method: "GET"
  //     });
  //     let resJson = await res.json();
  //     if (res.status === 200) {
  //       setMessageGroups(resJson)
  //     } else {
  //       console.log(res)
  //     }
  //   } catch (err) {
  //     console.log(err);
  //   }
  // };
  const url = `${process.env.REACT_APP_BACKEND_URL}/api/message_groups`
  get(url,{
    auth: true,
    success: function(data){
      setMessageGroups(data)
    }
    })
  }  

  const loadMessageGroupData = async () => {
  //   try {
  //     const handle = `${params.message_group_uuid}`;
  //     const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/messages/${handle}`
  //     await getAccessToken()
  //     const access_token = localStorage.getItem("access_token")
  //     const res = await fetch(backend_url, {
  //       headers: {
  //         Authorization: `Bearer ${access_token}`
  //       },
  //       method: "GET"
  //     });
  //     let resJson = await res.json();
  //     if (res.status === 200) {
  //       setMessages(resJson)
  //     } else {
  //       console.log(res)
  //     }
  //   } catch (err) {
  //     console.log(err);
  //   }
  // };  
  const url = `${process.env.REACT_APP_BACKEND_URL}/api/messages/${params.message_group_uuid}`
  get(url,{
    auth: true,
    success: function(data){
      setMessages(data)
    }
    })
  }

  // const checkAuth = async () => {
  //   console.log('checkAuth')
  //   // [TODO] Authenication
  //   if (Cookies.get('user.logged_in')) {
  //     setUser({
  //       display_name: Cookies.get('user.name'),
  //       handle: Cookies.get('user.username')
  //     })
  //   }
  // };

  React.useEffect(()=>{
    //prevents double call
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    loadMessageGroupsData();
    loadMessageGroupData();
    // checkAuth();
    checkAuth(setUser);
  }, [])
  return (
    <article>
      <DesktopNavigation user={user} active={'home'} setPopped={setPopped} />
      <section className='message_groups'>
        <MessageGroupFeed message_groups={messageGroups} />
      </section>
      <div className='content messages'>
        <MessagesFeed messages={messages} />
        <MessagesForm setMessages={setMessages} />
      </div>
    </article>
  );
}