import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { v4 as uuidv4 } from "uuid";
import "./App.css";

function Conference() {
    let { id } = useParams()
    let path = `http://localhost:9999?roomId=${id}`
  return (
    <div className="StartConference">
      <div style={{ width: "100%", height: "100vh", overflow: "hidden" }}>
        <iframe
          src={path}
          width="100%"
          height="80%"
          style={{ border: "none" }}
        />
      </div>
    </div>
  );
}

export default Conference;
