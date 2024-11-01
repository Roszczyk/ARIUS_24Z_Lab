import StarRating from '../StarRating';
import { FaTrash } from 'react-icons/fa';
import { HiCheck, HiPencil } from "react-icons/hi";

export default function Task({ id, title, details, deadline, status, stars, onRemove = f => f, onRate = f => f, onChangeStatus = f => f }) {
  const finalStatus = (status === "niewykonane" && new Date(deadline).getTime() < Date.now()) ? "przeterminowane" : status;
  const buttonText = finalStatus === "wykonane" ? "Nie wykonane" : "Wykonane";
  const buttonIcon = finalStatus === "wykonane" ? <HiPencil /> : <HiCheck />;
  const showRemoveButton = finalStatus !== "niewykonane";

  return (
    <section>
      <h1>{title}</h1>
      <div><b>Szczegóły:</b> {details}</div>
      <div><b>Deadline:</b> {deadline}</div>
      <div><b>Status:</b> {finalStatus}</div>
      <StarRating 
          selectedStars={stars}
          onRate={(stars) => onRate(id, stars)}    
      />
      <br/>
      {showRemoveButton && (
        <button onClick={() => onRemove(id)}>
          <div><FaTrash /><br />Usuń zadanie</div>
        </button>
      )}
      <button onClick={() => onChangeStatus(id)}>
        <div>{buttonIcon}<br />{buttonText}</div>
      </button>
    </section>
  );
}