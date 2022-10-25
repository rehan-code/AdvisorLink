import Logo from '../static/logo_img.png';

const Navbar = () => {
    return (
        <div className="w-screen flex justify-center items-center p-6 z-10" id='Navbar'>
            <div className="w-screen flex bg-white justify-between">
                <div className="flex justify-center items-center gap-4">
                    <div>
                        <img src={Logo} alt="advisorlink logo"/>
                    </div>
                    <div className="text-5xl"><strong>Advisor</strong>Link</div>
                </div>
                <div className="flex justify-center items-center gap-6 text-3xl">
                    <div><a href='/'>Calendar</a></div>
                    <div><a href='/'>About Us</a></div>
                    <div><a href='/'>Contact</a></div>
                </div>
            </div>
        </div>
    )
}

export default Navbar;