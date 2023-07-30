import { useState, useEffect } from "react";
import MusicSvg from "../../assets/svg/undraw_compose_music_re_wpiw.svg"
import axios from "axios";

function Home() {
    const [userCount, setUserCount] = useState(-1);
    const [scoreCount, setScoreCount] = useState(-1);

    useEffect(()=>{
        const getCounts = async () => {
            const API_URI = import.meta.env.VITE_API_URI;
            try {
                const response = await axios.get(`${API_URI}/api/util/user_count`);

                if (response.status === 200) {
                    setUserCount(response.data)
                } else {
                    console.error(response.data);
                }
            } catch (err) {
                setUserCount(-1)
            }

            try {
                const response = await axios.get(`${API_URI}/api/util/score_count`);

                if (response.status === 200) {
                    setScoreCount(response.data)
                } else {
                    console.error(response.data);
                }
            } catch (err) {
                setScoreCount(-1)
            }
        };

        getCounts();

    }, [])

    return <div className="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12">

        <div className="relative bg-white px-6 pt-5 pb-8 shadow-xl ring-1 ring-gray-900/5 sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10 ">

            <div className="grid grid-cols-2 gap-4">

                <div className="w-46">
                </div>

                <div className="grid grid-cols-1 w-60 gap-12  rounded-md px-2">
                    <div className="py-6 px-4 text-2xl">Users Count: <span className="font-extrabold bg-gradient-to-tr from-emerald-500 to-violet-600 bg-clip-text text-transparent">{userCount}</span></div>
                    <div className="py-6 px-4 text-2xl">Scores Count:<span className="font-extrabold bg-gradient-to-tr from-emerald-500 to-violet-600 bg-clip-text text-transparent">{scoreCount}</span></div>
                    <div className="py-6 px-4 text-2xl">Finished Purchase:<span className="font-extrabold bg-gradient-to-tr from-emerald-500 to-violet-600 bg-clip-text text-transparent">0</span></div>
                </div>
            </div>

            <img className="absolute -left-32 -top-32" src={MusicSvg} width="400" />

        </div>



    </div>
  
}

export default Home;