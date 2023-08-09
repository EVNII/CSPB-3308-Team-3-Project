import { useContext, useState } from "react";
import LoginContext from "../../context/LoginContext";
import { Link } from "react-router-dom";
import avater from '../../assets/svg/undraw_drink_coffee_v3au.svg'

function NavBar() {
    const loginContext = useContext(LoginContext);
    const [isHidden, setHidden] = useState(true);

    let button = <Link className="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 sm:mt-0" to='/login'>Login</Link>
    let hiddenclass = ''

    if (loginContext.islogin) {
        button = <div className="grid grid-cols-2 bg-white px-2 py-1 rounded-full  hover:bg-teal-300">
            <img src={avater} className="h-12 bg-white rounded-full border-teal-200 border-2" />
            <span onClick={() => {
                localStorage.removeItem('token');
                window.location.reload(false);
            }} className="px-3 place-self-center text-lg text-white underline underline-offset-4 hover:no-underline hover:bg-white rounded-full hover:text-teal-300 py-1 bg-teal-400">{loginContext.userInfo.username}</span>
        </div>
    }
    if (isHidden) {
        hiddenclass = 'hidden'
    }

    return <>
        <nav className="flex items-center justify-between flex-wrap bg-teal-500 p-6">
            <div className="flex items-center flex-shrink-0 text-white mr-6">
                <svg className="fill-current h-8 w-8 mr-2" width="54" height="54" viewBox="0 0 54 54" xmlns="http://www.w3.org/2000/svg"><path d="M13.5 22.1c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05zM0 38.3c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05z" /></svg>
                <span className="font-semibold text-xl tracking-tight">Music Verse</span>
            </div>
            <div className="block sm:hidden" onClick={() => { setHidden(!isHidden) }}>
                <button className="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white" >
                    <svg className="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" /></svg>
                </button>
            </div>
            <div className={`w-full ${hiddenclass} block flex-grow sm:flex sm:items-center sm:w-auto`}>
                <div className="text-sm sm:flex-grow">
                    <Link to="/" className="block mt-4 sm:inline-block sm:mt-0 text-teal-200 hover:text-white mr-4 sm:mb-0 mb-4">
                        Home
                    </Link>
                    <Link to="/user/" className="block mt-4 sm:inline-block sm:mt-0 text-teal-200 hover:text-white mr-4 sm:mb-0 mb-4">
                        Users
                    </Link>
                    <Link to="/score/" className="block mt-4 sm:inline-block sm:mt-0 text-teal-200 hover:text-white mr-4 sm:mb-0 mb-4">
                        Scores
                    </Link>
                    {
                        loginContext.islogin && <Link to="/upload" className="block mt-4 sm:inline-block sm:mt-0 text-teal-200 hover:text-white mr-4 sm:mb-0 mb-4">
                            Upload
                        </Link>
                    }
                </div>
                <div>
                    {button}
                </div>
            </div>
        </nav>
    </>
}

export default NavBar;