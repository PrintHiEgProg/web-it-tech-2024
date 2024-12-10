import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import StartConference from "./StartConference";
import Conference from "./Conference";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/conf" element={<StartConference />}/>
          <Route path="/conf/:id" element={<Conference />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
