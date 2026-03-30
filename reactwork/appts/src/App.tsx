import './App.css'
import CustomerComponent from './components/CustomerComponent'

function App() {
  let message: string = "Customer Details";
  return (
    <div>
      <h1>{message}</h1>
      <hr />
      <CustomerComponent />
    </div>
  )
}

export default App
