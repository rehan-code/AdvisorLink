function NotFound() {
  return (
    <div className="flex justify-center items-center w-full">
      <div className="flex flex-col gap-6 justify-center items-center p-6 bg-white w-7/12 text-xl rounded-md">
        <h1 className="text-4xl font-bold">404 - Not Found!</h1>
        <p>Sorry, the page you are looking for does not exist.</p>
      </div>
    </div>
  );
}

export default NotFound;
