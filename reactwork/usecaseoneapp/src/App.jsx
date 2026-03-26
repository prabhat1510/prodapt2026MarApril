import HelloWorldComponent from "./components/HelloWorldComponent";
import HelloMessageComponent from "./components/HelloMessageComponent";
import LoginComponent from "./components/LoginComponent";
import Counter from "./components/Counter";
import CustomerListComponent from "./components/CustomerListComponent";


function App() {
    const name = 'Euler';
    const message = "Message from ";
    const defaultMsg = ": Hi, Hello";
    let loginDetails = { username: "Euler", password: "1234" }

    return (
        <>
            <h3>Use Case -1 Components,Props,State</h3>
            <HelloWorldComponent />
            <HelloMessageComponent personName={name} msg={message} defaultMsg={defaultMsg} />
            {/*<LoginComponent loginDetails={loginDetails} />*/}
            <Counter />
            <CustomerListComponent />
        </>
    )
}

export default App