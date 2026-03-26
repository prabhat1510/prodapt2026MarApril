import bjp from "../assets/bjp.jfif";
import { Link } from "react-router-dom";
function BJPComponent() {
    return (
        <div>
            <h1>BJP Component</h1>
            <Link to="/" className="btn btn-primary">Home</Link>
            <img src={bjp} alt="bjp" width="100" height="100" />
        </div>
    )
}

export default BJPComponent