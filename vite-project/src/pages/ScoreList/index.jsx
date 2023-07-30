import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function ScoreList() {
    const [isLoading, setIsLoading] = useState(true);
    const [scores, setScores] = useState([]);

    useEffect(() => {
        const getUserLists = async () => {
            try {
                const API_URI = import.meta.env.VITE_API_URI;
                const response = await axios.get(`${API_URI}/api/score/all/`);

                if (response.status === 200) {
                  setScores(response.data)
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

            {scores &&  scores.map((score, key) => (<div key={key} className="grid grid-cols-2 gap-8 border-b-2">
                    <div className="grid-cols- mx-2 my-2 grid gap-0">
                        <Link className="py-2 text-2xl font-bold" to={`/score/${score.score_id}`}>{score.track_title}</Link>
                        <div>{score.username}</div>
                    </div>
                </div>))}

            </div>
        </div>
    </div>
}

export default ScoreList;