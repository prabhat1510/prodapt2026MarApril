import "./Hello.css";
function HelloMessageComponent(props) {
    /*const name = 'Euler';
    const message = "Message from ";
    const defaultMsg = ": Hi, Hello";*/

    //props.msg = "Hello"
    return (
        <div className="hello-world">
            <h1>{props.msg}{props.personName}{props.defaultMsg}</h1>
        </div>
    )
}

export default HelloMessageComponent