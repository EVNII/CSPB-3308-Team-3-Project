import { useState, useContext } from "react";
import axios from 'axios';
import { Link, useNavigate } from "react-router-dom";
import LoginContext from "../../context/LoginContext";

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const loginContext = useContext(LoginContext)
    const nav = useNavigate()


    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const API_URI = import.meta.env.VITE_API_URI;

            const response = await axios.post(`${API_URI}/api/user/login`,
                {
                    username,
                    password,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                        'accept': 'application/json'
                    }
                }

            );
            localStorage.setItem('token', response.data.access_token);

        } catch (error) {
            if (error.response) {
                setError(error.response.data.message)
            }
            return
        }

        nav('/');
        nav(0);

    };

    return <>
        {
            loginContext.islogin ?
                <div className="bg-orange-100 border-l-4 border-orange-500 text-orange-700 p-4 mx-4 my-6" role="alert">
                    <p className="font-bold">Warning!</p>
                    <p>You have logged in!</p>
                </div>
                :
                <div className="w-full md:h-screen flex justify-center md:items-center">
                    <form onSubmit={handleSubmit} className="bg-white lg:shadow-lg rounded px-8 pt-6 pb-8 mb-4">
                        <div className="mb-1">
                            <label className=" text-gray-400">
                                Username:
                            </label>
                        </div>
                        <div className="mb-4">
                            <input
                                type="text"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                required
                                placeholder="Username"
                                className="shadow appearance-none border rounded w-full text-gray-800 py-2 px-2 leading-5 focus:outline-3 focus:shadow-none"
                            />
                        </div>
                        <div className="mb-1">
                            <label className=" text-gray-400">
                                Password:
                            </label>
                        </div>
                        <div className="mb-4">
                            <input
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                                placeholder="Password"
                                className="shadow appearance-none border rounded w-full text-gray-800 py-2 px-2 leading-5 focus:outline-3 focus:shadow-none"
                            />
                        </div>
                        <div>
                            {error && <><small style={{ color: 'red' }}>{error}</small><br /></>}<br />
                            <div className="grid grid-cols-2 justify-items-center items-center">
                            <button  type="submit"
                                className=" bg-teal-300 py-2 px-4 rounded text-white text-md hover:outline-teal-300 hover:bg-white hover:outline hover:text-teal-500"
                            >Log In</button>
                            <Link to='/signup' className=" underline text-teal-300 hover:text-teal-400">Sign up</Link>
                            </div>
                        </div>
                    </form>
                </div>

        }

    </>

}

export default Login;
