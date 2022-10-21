export default (req, res) => {
  fetch("http://backend-flask:5000/api/comic")
    .then((response) => response.json())
    .then((data) => res.status(200).json(data));
};
