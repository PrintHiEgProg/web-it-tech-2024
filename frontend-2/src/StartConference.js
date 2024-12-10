import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { v4 as uuidv4 } from "uuid";
import "./App.css";

function StartConference() {
  const navigate = useNavigate()
  const [path, setPath] = useState("");

  const StartLive = () => {
    const newPath = `/conf/${uuidv4()}`;
    navigate(newPath);
  };

  return (
    <div className="StartConference">
      <button onClick={StartLive}>Начать вебинар</button>
    </div>
  );
}

export default StartConference;
