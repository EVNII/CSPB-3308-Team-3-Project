import { useState, useEffect, useContext } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import LoginContext from "../../context/LoginContext";


function ScoreDetail() {
  const [score, setScore] = useState();
  const [author, setAuthor] = useState();
  const [isLoading, setIsLoading] = useState(true);
  const { id } = useParams();
  const loginCtx = useContext(LoginContext)
  const API_URI = import.meta.env.VITE_API_URI;

  useEffect(() => {
    const fetchUserData = async () => {
      const response = await axios.get(`${API_URI}/api/score/${id}`);

      setAuthor(response.data.author)
      setScore(response.data.score)

      setIsLoading(false)
    }
    fetchUserData()
  }, [])


  const ViewPDF = async () => {
    await axios.get(`${API_URI}/api/score/pdf/${id}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      },
      responseType: 'blob',
    }).then(response => {
      const blob = new Blob([response.data], { type: 'application/pdf' });

      if (window.navigator && window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveOrOpenBlob(response.data, "test.pdf");
        return;
      }

      // Chrome, FF
      const fileUrl = URL.createObjectURL(blob);

      if (navigator.userAgent.indexOf('Chrome') != -1 || navigator.userAgent.indexOf('Firefox') != -1) {
        const w = window.open(fileUrl, '_blank');
        w && w.focus();
      } else {
        // Safari & Opera iOS
        window.location.href = fileUrl;
      }

    }
    )
    // IE
  }

  // if you want to support Safari & Opera iOS version


  return isLoading ? <div>Loading</div> : <div className="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12">
    <div className="relative bg-white px-6 pb-8 pt-5 shadow-xl ring-1 ring-gray-900/5 sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
      <div className="grid grid-cols-1 gap-8">
        <div className="grid grid-cols-2 gap-10 border-b-2 py-6">
          <div className="gpa-1 grid grid-cols-1">
            <div className="text-2xl font-bold">{score.track_title}</div>
            <div className="text-gray-500">{author.username}</div>
            {
              loginCtx.islogin &&
              <div onClick={ViewPDF}>
                View PDF
              </div>
            }
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="gpa-1 grid grid-cols-1">
            <div className="text-2xl font-bold">Price: </div>
            <div className="bg-gradient-to-bl from-teal-400 to-blue-700 bg-clip-text text-4xl font-extrabold text-transparent">${score.price}</div>
          </div>

          <div className="gpa-1 grid grid-cols-1">
            <div className="text-2xl font-bold">Downloads</div>
            <div className="bg-gradient-to-bl from-teal-400 to-blue-700 bg-clip-text text-4xl font-extrabold text-transparent">{score.downloads}</div>
          </div>
        </div>
      </div>
    </div>
  </div>

}

export default ScoreDetail;