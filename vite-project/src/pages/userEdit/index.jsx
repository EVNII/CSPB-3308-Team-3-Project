import { useState, useEffect, useContext } from "react";
import axios from "axios";
import LoginContext from "../../context/LoginContext";
import { useNavigate } from "react-router-dom";


function UserEdit() {
  const [user, setuser] = useState({});
  const [editInfo, setEditInfo] = useState({
    'username': "",
    'password': "",
    'surname': "",
    'firstname': "",
    'active': true,
    'recovery_question': "",
    'recovery_answer': ""
  })

  const setEditInfoState = (field, value) => {
    setEditInfo(prevState => ({
      ...prevState,
      [field]: value
    }))
  }

  const nav = useNavigate()

  const [isLoading, setIsLoading] = useState(true);
  const loginCtx = useContext(LoginContext)

  let user_id = -1;

  if (loginCtx.islogin) {
    user_id = loginCtx.userInfo.user_id
  }

  useEffect(() => {
    console.log(editInfo)
  }, [editInfo])

  useEffect(() => {
    const fetchUserData = async () => {

      const token = localStorage.getItem('token');
      const API_URI = import.meta.env.VITE_API_URI;
      const response = await axios.get(`${API_URI}/api/user/account/${user_id}`,
      {
        headers: {
          'Content-Type': 'application/json',
          'accept': 'application/json',
          Authorization: `Bearer ${token}`
      }
      }
      );

      setuser(response.data)

      setIsLoading(false)
    }
    setIsLoading(true)
    if (loginCtx.islogin) {
      fetchUserData()
    } else {
      setIsLoading(false)
    }

  }, [loginCtx])

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
        const token = localStorage.getItem('token');

        const API_URI = import.meta.env.VITE_API_URI;
        var newInfo = editInfo;
        for(let k in newInfo)
          if( newInfo[k] == '' )
            delete newInfo[k]

        await axios.put(`${API_URI}/api/user/account/${user_id}`,
            newInfo,
            {
                headers: {
                    'Content-Type': 'application/json',
                    'accept': 'application/json',
                    Authorization: `Bearer ${token}`
                }
            }

        );

    } catch (error) {
        if (error.response) {
            console.log(error.response.data)
        }
        return
    }

    nav(0);

};

  return isLoading ? <div>Loading</div> : (loginCtx.islogin ?
    <div className="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12">
      <div className="relative bg-white px-6 pb-8 pt-5 shadow-xl ring-1 ring-gray-900/5 sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
        <div className="grid grid-cols-1 gap-8">

          <form onSubmit={handleSubmit}>
            <div className="mb-1">
              <label>Username</label>
            </div>
            <div className="mb-4">
              <input
                type="text"
                value={editInfo.username}
                onChange={(e) => { setEditInfoState('username', e.target.value) }}
                placeholder={user.username}
              />
            </div>

            <div className="mb-1">
              <label>Password</label>
            </div>
            <div className="mb-4">
              <input
                type="password"
                value={editInfo.password}
                onChange={(e) => { setEditInfoState('password', e.target.value) }}
                placeholder="password"
              />
            </div>

            <div className="mb-1">
              <label>surname</label>
            </div>
            <div className="mb-4">
              <input
                type="text"
                value={editInfo.surname}
                onChange={(e) => { setEditInfoState('surname', e.target.value) }}
                placeholder={user.surname}
              />
            </div>

            <div className="mb-1">
              <label>First Name:</label>
            </div>
            <div className="mb-4">
              <input
                type="text"
                value={editInfo.firstname}
                onChange={(e) => { setEditInfoState('firstname', e.target.value) }}
                placeholder={user.firstname}
              />
            </div>

            <div className="mb-1">
              <label>Active:</label>
            </div>
            <div className="mb-4">
              <input
                type="checkbox"
                onChange={(e) => { setEditInfoState('active', e.target.checked) }}
                defaultChecked={true}
              />
            </div>

            <div className="mb-1">
              <label>Recovery Question:</label>
            </div>
            <div className="mb-4">
              <input
                type="text"
                value={editInfo.recovery_question}
                onChange={(e) => { setEditInfoState('recovery_question', e.target.value) }}
                placeholder={user.recovery_question}
              />
            </div>

            <div className="mb-1">
              <label>Recovery Answer:</label>
            </div>
            <div className="mb-4">
              <input
                type="text"
                value={editInfo.recovery_answer}
                onChange={(e) => { setEditInfoState('recovery_answer', e.target.value) }}
                placeholder={user.recovery_answer}
              />
            </div>

            <button type="submit"
              className=" bg-teal-300 py-2 px-4 rounded text-white text-md hover:outline-teal-300 hover:bg-white hover:outline hover:text-teal-500"
            >Save</button>
          </form>

        </div>
      </div>
    </div>
    :
    <div>No login Information</div>)
}

export default UserEdit;