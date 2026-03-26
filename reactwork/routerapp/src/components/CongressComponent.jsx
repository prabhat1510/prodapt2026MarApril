import congress from "../assets/congress.png";
import { Link } from "react-router-dom";
function CongressComponent() {
    return (
        <div>
            <h1>Congress Component</h1>
            <Link to="/" className="btn btn-primary">Home</Link>
            <img src={congress} alt="congress" width="100" height="100" />
        </div>
    )
}

export default CongressComponent    