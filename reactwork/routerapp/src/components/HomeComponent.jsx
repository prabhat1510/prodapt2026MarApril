import { Link } from "react-router-dom";
function HomeComponent() {
    return (
        <div>
            <div className="d-flex justify-content-center gap-3 mb-4">
                <Link to="/bjp" className="btn btn-primary">BJP</Link>
                <Link to="/dmk" className="btn btn-success">DMK</Link>
                <Link to="/tmc" className="btn btn-warning">TMC</Link>
                <Link to="/congress" className="btn btn-danger">Congress</Link>
                <Link to="/tvk" className="btn btn-info">TVK</Link>
            </div>
        </div>
    )
}

export default HomeComponent