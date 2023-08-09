import { useState, useContext, useEffect} from "react";
import axios from "axios";
import LoginContext from "../../context/LoginContext";
import { useNavigate } from "react-router-dom";


function UploadPDF() {
  const loginContext = useContext(LoginContext)
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    title: "",
    author: "",
    genre: "",
    price: "",
    pdfFile: null,
  });
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setFormData((prevData) => ({ ...prevData, pdfFile: file }));
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    const formDataToSend = new FormData();
    formDataToSend.append("track_title", formData.title);
    formDataToSend.append("instrument", formData.author);
    formDataToSend.append("genre", formData.genre);
    formDataToSend.append("price", formData.price ? formData.price.toString() : "0");
    formDataToSend.append("file", formData.pdfFile);

    try {
      const API_URI = import.meta.env.VITE_API_URI;
      await axios.post(`${API_URI}/api/score/upload`, formDataToSend, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
          "Content-Type": "multipart/form-data",
        },
      });

      // Reset the form after successful submission
      setFormData({
        title: "",
        author: "",
        genre: "",
        price: "",
        pdfFile: null,
      });

      // Show a success message or perform any other actions after successful submission
      alert("Score uploaded successfully!");
    } catch (error) {
      console.error("Error uploading the form data and PDF.", error);
      // Show an error message or perform any other error-handling actions
      if (error.response) {
        setError(error.response.data.message);
      }
      return;
    }
  };

useEffect(()=>{
  if (loginContext.islogin == false){
      navigate("/login")
  }
}, []

)

  return (
    <div className="min-h-screen">
      <div className="max-w-4xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <div className="bg-teal-500 py-4 px-6 rounded-t-lg">
            <h2 className="text-2xl font-bold text-white">Upload PDF</h2>
          </div>
          <div className="p-6">
            <form onSubmit={handleFormSubmit}>
              <div className="mb-4">
                <label htmlFor="title" className="block text-gray-700 font-bold mb-2">
                  Title
                </label>
                <input
                  type="text"
                  id="title"
                  name="title"
                  placeholder="Enter title..."
                  value={formData.title}
                  onChange={handleInputChange}
                  className="border border-gray-400 rounded w-full py-2 px-3 focus:outline-none focus:ring focus:border-green-500"
                />
              </div>
              <div className="mb-4">
                <label htmlFor="author" className="block text-gray-700 font-bold mb-2">
                  Instrument
                </label>
                <input
                  type="text"
                  id="author"
                  name="author"
                  placeholder="Enter author..."
                  value={formData.author}
                  onChange={handleInputChange}
                  className="border border-gray-400 rounded w-full py-2 px-3 focus:outline-none focus:ring focus:border-green-500"
                />
              </div>
              <div className="mb-4">
                <label htmlFor="genre" className="block text-gray-700 font-bold mb-2">
                  Genre
                </label>
                <input
                  type="text"
                  id="genre"
                  name="genre"
                  placeholder="Enter genre..."
                  value={formData.genre}
                  onChange={handleInputChange}
                  className="border border-gray-400 rounded w-full py-2 px-3 focus:outline-none focus:ring focus:border-green-500"
                />
              </div>
              <div className="mb-4">
                <label htmlFor="genre" className="block text-gray-700 font-bold mb-2">
                  Price
                </label>
                <input
                  type="text"
                  id="price"
                  name="price"
                  placeholder="Enter price..."
                  value={formData.price}
                  onChange={handleInputChange}
                  className="border border-gray-400 rounded w-full py-2 px-3 focus:outline-none focus:ring focus:border-green-500"
                />
              </div>
              <div className="mb-4">
                <input
                  type="file"
                  accept=".pdf"
                  onChange={handleFileChange}
                  className="border border-gray-400 rounded w-full py-2 px-3 focus:outline-none focus:ring focus:border-green-500"
                />
              </div>
              <button
                type="submit"
                className="bg-teal-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded"
              >
                Publish
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UploadPDF;
