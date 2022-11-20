function About() {
  return (
    <div className="h-screen flex items-center justify-center w-full">
      <div className="bg-white w-10/12 p-10 rounded-md">
        <div className="w-full flex flex-col items-center justify-center gap-5">
          <h1 className="text-4xl font-bold">About Us</h1>
          <h2 className="text-xl font-semibold">Team Members</h2>
          <div className="grid grid-cols-2 gap-12">
            <div>
              <h1>Rehan Nagoor Mohideen</h1>
              <h1>Alif Merchant</h1>
              <h1>Ivan Magtangob</h1>
              <h1>Muhammad Salmaan</h1>
            </div>
            <div>
              <h1>Hyrum Nantais</h1>
              <h1>Samuel Guilbeault</h1>
              <h1>Parker Carnegie</h1>
              <h1>Caleb Beere</h1>
            </div>
          </div>
          <h2 className="text-xl font-semibold">Software</h2>
          <div className="w-7/12">
            <p>
              AdvisorLink is a utility that makes selecting and scheduling
              courses easy. AdvisorLink is a webapp that leverages React and
              Flask to offer a reliable, flexible, and easy to use scheduling
              software. The app is running on an Azure Debian-based Linux VM
              that serves both the front and backend using NGINX.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default About;
