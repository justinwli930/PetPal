import React from "react";
import { LogoToLandingButton } from "./LogoToLandingButton";
import { useState, useRef, useContext } from "react";
import { Link, useLocation } from "react-router-dom";

export default function NavBar({}) {
    // const location = useLocation();

    const isAuthenticated = true;
    const isShelter = true;
    const hasNotification = true;
    const selectedTab = "";

    let contentRef = useRef(null);
    let iconOpenRef = useRef(null);
    let iconCloseRef = useRef(null);

    const [isActive, setIsActive] = useState(false);

    function toggleNavBar() {
        setIsActive(current => !current);
    }
    const contentMaxHeight = isActive ? `${contentRef.current.scrollHeight}px` : null;
    const iconDisplayStyleOpen = isActive ? 'block' : 'none';
    const iconDisplayStyleClose = isActive ? 'none' : 'block';

    return (
        <header>
            <div className="hidden bg-[#FFF8F4] lg:flex lg:flex-row flex-nowrap gap-[2rem] justify-between text-[1rem]">
                {/* <!-- normal navbar start --> */}
                <div className=" flex flex-row text-[2rem] items-center pl-[1.5rem]">
                    <LogoToLandingButton/>
                    <Link to="/" className={`hover:border-b-[1rem] hover:border-[#290005] hover:pb-[1.65rem] self-end text-[1rem] font-medium px-[2rem] ml-[1rem] hover:cursor-pointer` + ((selectedTab === "home") ? " border-[#290005] border-b-[1.65rem] pb-[1.65rem]" : " pb-[2.65rem]")}>
                        Home
                    </Link>
                    <Link to="/search" className={"hover:border-b-[1rem] hover:border-[#290005] hover:pb-[1.65rem] self-end text-[1rem] font-medium px-[2rem] hover:cursor-pointer" + ((selectedTab === "search") ? " border-[#290005] border-b-[1rem] self-end pb-[1.65rem]" : " pb-[2.65rem]")}>
                        Adopt
                    </Link>
                    
                </div>

                
                { (isAuthenticated) ? (
                    <div className="self-center flex flex-row gap-[1rem] pr-[1.5rem] font-semibold items-center">
                        {((isShelter) ? (
                            <Link to="/listings">
                                <div class="mx-[1rem] font-medium hover:cursor-pointer border-b-[3px] border-[#FF9447] hover:border-[#290005]">My Listings</div>
                            </Link>
                        ) : (null))}
                        {((hasNotification) ? (
                            <Link to='/notifications' class="bg-[#FF9447] hover:opacity-[80%] transition duration-300 py-[.5rem] rounded-full px-[.5rem]" id="notificationButton">
                                <img class="w-[2rem] h-[2rem]" src="/notification.svg"/>
                            </Link>
                        ) : (null))}
                        <Link to="/profile"
                            className="hover:opacity-[80%] transition bg-[#FF9447] py-[1.2rem] px-[1rem] w-[10rem] text-center text-[#FFF8F4] hover:cursor-pointer rounded-full flex flex-nowrap justify-center items-center space-x-2">
                            <img src="/profile_icon.svg" alt="profile_icon.svg" className="h-6 w-6"/>
                            <span>My Profile</span>
                        </Link>
                    </div>
                ) : (
                    <div class="self-center flex flex-row gap-[1rem] pr-[1.5rem] font-semibold">
                        <Link to="/signup">
                            <div class="bg-[#FF9447] py-[.75rem] w-[8rem] text-center text-[#FFF8F4] hover:opacity-[85%] transition">
                                Sign Up
                            </div>
                        </Link>
                        <Link to="/login" class="border-[#290005] border-[1px] py-[.75rem] w-[8rem] text-center text-[#290005] hover:cursor-pointer hover:bg-[#290005] hover:text-white transition duration-300">
                            Log In
                        </Link>
                    </div>
                )
                }
                    
                
            </div>
            <div className="lg:hidden bg-[#FFF8F4]">
                {/* <!-- mobile navbar start --> */}
                <div className="flex flex-row flex-nowrap justify-between px-[1.5rem]  text-[1rem]">
                    <LogoToLandingButton/>
                    <div className="self-center">
                        <button type="button" id="navBarCollapsible" onClick={toggleNavBar} className="cursor-pointer">
                            <svg id="navBarCollapsibleClosed" ref={iconCloseRef}  xmlns="http://www.w3.org/2000/svg" width="42" height="40" style={{ display: iconDisplayStyleClose }}
                                viewBox="0 0 42 40" fill="none">
                                <path fill-rule="evenodd" clip-rule="evenodd"
                                    d="M2.24999 4.33329H39.75C40.9006 4.33329 41.8333 3.40055 41.8333 2.24996C41.8333 1.09937 40.9006 0.166626 39.75 0.166626H2.24999C1.0994 0.166626 0.166656 1.09937 0.166656 2.24996C0.166656 3.40055 1.0994 4.33329 2.24999 4.33329ZM41.8333 37.6666C41.8333 38.8172 40.9006 39.75 39.75 39.75H2.24999C1.0994 39.75 0.166656 38.8172 0.166656 37.6666C0.166656 36.516 1.0994 35.5833 2.24999 35.5833H39.75C40.9006 35.5833 41.8333 36.516 41.8333 37.6666ZM2.24999 18.9166H39.75C40.9006 18.9166 41.8333 19.8494 41.8333 21C41.8333 22.1506 40.9006 23.0833 39.75 23.0833H2.24999C1.0994 23.0833 0.166656 22.1506 0.166656 21C0.166656 19.8494 1.0994 18.9166 2.24999 18.9166Z"
                                    fill="#290005" />
                            </svg>
                            <svg id="navBarCollapsibleOpen" ref={iconOpenRef}  className="hidden" xmlns="http://www.w3.org/2000/svg" width="42"  style={{ display: iconDisplayStyleOpen }}
                                height="42" viewBox="0 0 42 42" fill="none">
                                <path
                                    d="M41.2292 38.2708C41.6236 38.662 41.8454 39.1945 41.8454 39.75C41.8454 40.3055 41.6236 40.838 41.2292 41.2292C40.838 41.6236 40.3055 41.8454 39.75 41.8454C39.1945 41.8454 38.662 41.6236 38.2708 41.2292L21 23.9375L3.72918 41.2292C3.338 41.6236 2.80551 41.8454 2.25002 41.8454C1.69452 41.8454 1.16203 41.6236 0.770849 41.2292C0.376447 40.838 0.154602 40.3055 0.154602 39.75C0.154602 39.1945 0.376447 38.662 0.770849 38.2708L18.0625 21L0.770849 3.72915C0.242393 3.2007 0.0360079 2.43046 0.229436 1.70857C0.422864 0.98669 0.986719 0.422835 1.7086 0.229407C2.43049 0.0359789 3.20073 0.242364 3.72918 0.77082L21 18.0625L38.2708 0.77082C39.0878 -0.0461016 40.4123 -0.0461016 41.2292 0.77082C42.0461 1.58774 42.0461 2.91223 41.2292 3.72915L23.9375 21L41.2292 38.2708Z"
                                    fill="#290005" />
                            </svg>
                        </button>
                    </div>
                </div>
                <div id="navBarCollapsibleContent" ref={contentRef} className="overflow-hidden flex flex-col items-end"
                    style={{boxShadow: "0px 0px 18px 0px rgba(0, 0, 0, 0.1) inset", maxHeight: contentMaxHeight}}>
                    <div className="flex flex-col text-[1rem] w-[100%] font-semibold text-[290005]">
                        <Link to="/" className="border-b-[.05rem] border-[#6C6866] py-[1rem] mx-[1.5rem] grow">
                            <div className="px-[2rem] hover:cursor-pointer w-[100%] text-end">Home</div>
                        </Link>
                        <Link to="/search" className="border-b-[.05rem] border-[#6C6866] py-[1rem] mx-[1.5rem] grow">
                            <div className="px-[2rem] hover:cursor-pointer w-[100%] text-end">Adopt</div>
                        </Link>
                        {(isShelter) ? (
                            <Link to="/listings" class="border-b-[.05rem] border-[#6C6866] py-[1rem] mx-[1.5rem] grow">
                                <div class="px-[2rem] hover:cursor-pointer w-[100%] text-end hover:decoration-black">My Listings</div>
                            </Link>
                        ) : (
                            null
                        )}
                    </div>
                    { (isAuthenticated) ? (
                        <div className="flex flex-row justify-end gap-[1rem] mr-[1.5rem] w-[100%] py-[1rem] font-semibold">
                            {(hasNotification) ? (
                                <Link to="/notifications" class="bg-[#FF9447] hover:opacity-[80%] transition duration-300 py-[.5rem] rounded-full px-[.5rem]" id="notificationaMobile">
                                    <img class="w-[2rem] h-[2rem]" src="notification.svg"/>
                                </Link>
                            ) : (null)}
                            <Link to="/profile" className="bg-[#FF9447] py-[.75rem] w-[10rem] text-center text-[#FFF8F4] rounded-full flex flex-row gap-[.5rem] justify-center hover:opacity-[85%] transition duration-300">
                                <img src="profile_icon.svg" alt="profile_icon.svg" className="h-6 w-6"/>
                                My Profile
                            </Link>
                        </div>) : (
                        <div class="flex flex-row justify-end gap-[1rem] mr-[1.5rem] w-[100%] py-[1rem] font-semibold">
                            <Link to="/signup">
                                <div class="bg-[#FF9447] py-[.75rem] w-[8rem] text-center text-[#FFF8F4] hover:opacity-[85%] transition">
                                    Sign Up
                                </div>
                            </Link>
                            <Link to="/login" class="border-[#290005] border-[1px] py-[.75rem] w-[8rem] text-center text-[#290005] hover:bg-[#290005] hover:text-white transition duration-300">
                                Log In
                            </Link>
                        </div>
                    )
                    }
                </div>
                {/* <!-- mobile navbar end --> */}
            </div>
        </header>
    )
};