import axios from 'axios';
const INTERNSHIPS_API = 'https://coping-backend.herokuapp.com/internships';
// const INTERNSHIPS_API = 'http://localhost:8000/internships/';


export const findInternships = async () => {
    const response = await axios.get(INTERNSHIPS_API);
    const internships = response.data;
    return internships;
   }   


export const deleteInternship = async (id) => {
    const response = await axios.delete(`${INTERNSHIPS_API}/${id}`)
return response.data
}
export const createInternship = async (internship) => {
    const response = await axios.post(INTERNSHIPS_API, internship)
    return response.data;
}

export const updateInternship = async (internship) => {
    const response = await axios.put(`${INTERNSHIPS_API}/${internship.id}`, internship);
    return response.data;
}
  