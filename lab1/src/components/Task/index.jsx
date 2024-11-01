import StarRating from '../StarRating';

export default function Task ({id, title, details, deadline, status, stars})
{
  return(
    <section>
      <h1>{title}</h1>
      <div>Szczegóły: {details}</div>
      <div>Deadline: {deadline}</div>
      <div>Status: {status}</div>
      <StarRating selectedStars = {stars}/>
    </section>
  );
}