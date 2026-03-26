import tmc from "../assets/tmc.jfif";
import { Link } from "react-router-dom";
function TMCComponent() {
    return (
        <div>
            <h1>TMC Component</h1>
            <Link to="/" className="btn btn-primary">Home</Link>
            <img src={tmc} alt="tmc" width="100" height="100" />
        </div>
    )
}

export default TMCComponent 