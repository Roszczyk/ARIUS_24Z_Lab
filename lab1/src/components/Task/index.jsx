import StarRating from '../StarRating';
import { FaTrash } from 'react-icons/fa';

export default function Task ({id, title, details, deadline, status, stars, onRemove = f => f, onRate = f => f})
{
  if (status === "wykonane") return(
    <section>
      <h1>{title}</h1>
      <div><b>Szczegóły:</b> {details}</div>
      <div><b>Deadline:</b> {deadline}</div>
      <div><b>Status:</b> {status}</div>
      <StarRating 
          selectedStars = {stars}
          onRate = {stars => onRate(id,stars)}    
      />
      <br/>
      <button onClick = {() => onRemove(id)}>
        <div><FaTrash/><br/>Usuń zadanie</div>
      </button>
    </section>
  );
  else return(
    <section>
      <h1>{title}</h1>
      <div><b>Szczegóły:</b> {details}</div>
      <div><b>Deadline:</b> {deadline}</div>
      <div><b>Status:</b> {status}</div>
      <StarRating 
          selectedStars = {stars}
          onRate = {stars => onRate(id,stars)}    
      />
    </section>
  );
}