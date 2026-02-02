import axios from "axios";

const API = axios.create({
  baseURL: "https://fossee-backend-deepali.onrender.com",
});

export const uploadCSV = (formData) => {
  return API.post("/api/upload/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};
