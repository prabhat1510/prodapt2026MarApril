import tvk from "../assets/tvk.jfif";
import { Link } from "react-router-dom";
function TVKComponent() {
    return (
        <div>
            <h1>TVK Component</h1>
            <Link to="/" className="btn btn-primary">Home</Link>
            <img src={tvk} alt="tvk" width="100" height="100" />
        </div>
    )
}

export default TVKComponent