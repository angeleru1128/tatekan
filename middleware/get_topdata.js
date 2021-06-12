export default async function topdata_get(){
  const axiosBase = require("axios");
  const axios = axiosBase.create({
    baseURL: "http://127.0.0.1:5000",
    headers: {
      "Content-Type": "application/json",
      "X-Requested-With": "XMLHttpRequest",
    },
    responseType: "json"
  });
  let data = axios.get("/topdata");
  //console.dir(data);
  return data.data;
}