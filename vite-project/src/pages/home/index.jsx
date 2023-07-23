import { useContext } from 'react';
import { useNavigate, Link } from 'react-router-dom'
import LoginContext from '../../context/LoginContext';

function Home() {

    const loginCtx = useContext(LoginContext);

    return  <div className='flex items-stretch w-full h-screen bg-teal-50'>
            {
                loginCtx.islogin ?
                <a className="rounded-full" onClick={()=>{
                    localStorage.removeItem('token');
                    window.location.reload(false);
                }}>Log out</a>
                : <div className='flex text-cyan-500 text-center text-6xl h-full place-self-center'>
                    Welcome to Music Verse!
                </div>
            }
        </div>
}

export default Home;