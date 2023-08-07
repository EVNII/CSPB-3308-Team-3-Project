import { useState, useEffect, useContext } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import Avater from "../../assets/svg/undraw_drink_coffee_v3au.svg"
import LoginContext from "../../context/LoginContext";
import { Link } from "react-router-dom";


function UserProfile() {
    const [user, setuser] = useState();
    const [isLoading, setIsLoading] = useState(true);
    const {id} = useParams();
    const loginCtx = useContext(LoginContext)
    let isMyPage = false;

    if(loginCtx.islogin == true && loginCtx.userInfo.user_id == id){
      isMyPage=true;
    }

    useEffect(()=>{
      const fetchUserData = async () => {
        const API_URI = import.meta.env.VITE_API_URI;
        const response = await axios.get(`${API_URI}/api/user/account/${id}`);

        setuser(response.data)

        setIsLoading(false)
      }
      fetchUserData()
    },[])


    return isLoading ? <div>Loading</div> : <div className="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12">
      <div className="relative bg-white px-6 pb-8 pt-5 shadow-xl ring-1 ring-gray-900/5 sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
        <div className="grid grid-cols-1 gap-8">
          <div className="grid grid-cols-2 gap-10 border-b-2 py-6">
            <img src={Avater} className="rounded-full border-4" width="80" height="80" />
            <div className="gpa-1 grid grid-cols-1">
              <div className="text-2xl font-bold">{user.username}
              {isMyPage && <Link className="px-4 appearance-none border-cyan-300 bg-teal-300 mx-3 rounded-xl py-2 text-white" to='/user/edit/'>
                Edit
                </Link>}
              </div>
              <div className="text-gray-500"></div>
            </div>
          </div>
    
          <div className="grid grid-cols-2 gap-4">
            <div className="gpa-1 grid grid-cols-1">
              <div className="text-2xl font-bold">POST Scores</div>
              <div className="bg-gradient-to-bl from-teal-400 to-blue-700 bg-clip-text text-4xl font-extrabold text-transparent">11 (Mock)</div>
            </div>
    
            <div className="gpa-1 grid grid-cols-1">
              <div className="text-2xl font-bold">Purchase Scores</div>
              <div className="bg-gradient-to-bl from-teal-400 to-blue-700 bg-clip-text text-4xl font-extrabold text-transparent">12 (Mock)</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
}

export default UserProfile;