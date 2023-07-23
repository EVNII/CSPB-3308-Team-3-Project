import  {useEffect, useState} from "react";
import { RouterProvider } from "react-router-dom";
import { globalRouters } from "./router";
import LoginContext from "./context/LoginContext";
import axios from "axios";

const App = () => {

    const [logininfo, setLogininfo] = useState({
        islogin: false,
        userInfo: {}
    });

    useEffect(() => {
        const checkLoginStatus = async () => {
            const token = localStorage.getItem('token');

            if (!token) {
                logininfo.islogin = false;
                logininfo.userInfo = {};
            }

            try {
                const API_URI = import.meta.env.VITE_API_URI;
                const response = await axios.get(`${API_URI}/api/user/login_info`, {
                    headers: { Authorization: `Bearer ${token}` }
                });

                if (response.status === 200) {
                    setLogininfo(
                        {
                            islogin: true,
                            userInfo: response.data.logged_in_as,
                        }
                    )
                } else {
                    localStorage.removeItem('token');
                    setLogininfo(
                        {
                            islogin: false,
                            userInfo: {}
                        }
                    )
                }
            } catch (err) {
                console.error(err.message);
                localStorage.removeItem('token');
                setLogininfo(
                    {
                        islogin: false,
                        userInfo: {}
                    }
                )
            }
        };

        checkLoginStatus();
    }, []);


    return (
        <>
            <LoginContext.Provider value={logininfo}>
                
                <RouterProvider router={globalRouters}/>

            </LoginContext.Provider>
        </>
    )
}

export default App;