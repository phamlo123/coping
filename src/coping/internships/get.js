import axios from "axios";


async function RetrieveInternships(url)  {
    let array = []

    let response = await axios.get(url);
    let data = response.data;

    return array;
}


export default RetrieveInternships;