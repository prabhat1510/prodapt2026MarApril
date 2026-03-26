function DisplayListComponent() {
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    const listItems = numbers.map((number) =>
        <li key={number}>{number}</li>
    )
    return (
        <div>
            <h1>Display List</h1>
            <ul>
                {listItems}
            </ul>
        </div>
    )
}

export default DisplayListComponent