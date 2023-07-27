import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Avater from "../../assets/svg/undraw_drink_coffee_v3au.svg"


function UserList() {
    const [isLoading, setIsLoading] = useState(true);
    const [users, setUsers] = useState([]);

    useEffect(() => {
        const getUserLists = async () => {
            try {
                const API_URI = import.meta.env.VITE_API_URI;
                const response = await axios.get(`${API_URI}/api/user/account/`);

                if (response.status === 200) {
                    setUsers(response.data)
                } 
            } catch (err) {
                console.log("Error")
            }

        
        };

        getUserLists();
        setIsLoading(false)
        
    }, [])

    

    return isLoading ? <>Loaing!</> : <div className="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12">
        <div className="relative bg-white px-6 pb-8 pt-5 shadow-xl ring-1 ring-gray-900/5 sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
            <div className="grid grid-cols-1 gap-4">

            {users &&  users.map((user, key) => (<div key={key} className="grid grid-cols-2 gap-8 border-b-2">
                    <img src={Avater} className="mx-2 my-2 rounded-full border-4" width="80" height="80" />
                    <div className="grid-cols- mx-2 my-2 grid gap-0">
                        <Link className="py-2 text-2xl font-bold" to={`/user/${user.id}`}>{user.username}</Link>
                        <div>Email: {user.email}</div>
                    </div>
                </div>))}

            </div>
        </div>
    </div>
}

export default UserList;