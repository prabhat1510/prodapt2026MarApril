import dmk from "../assets/dmk.jfif";
import { Link } from "react-router-dom";
function DMKComponent() {
    return (
        <div>
            <h1>DMK Component</h1>
            <Link to="/" className="btn btn-primary">Home</Link>
            <img src={dmk} alt="dmk" width="100" height="100" />

        </div>
    )
}

export default DMKComponent 