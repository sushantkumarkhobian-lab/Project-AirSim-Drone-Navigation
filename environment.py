import os
from projectairsim import ProjectAirSimClient, Drone, World
from projectairsim.utils import projectairsim_log
from projectairsim.types import WeatherParameter


# ==============================
# COLOR CODES
# ==============================

RESET   = "\033[0m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
MAGENTA = "\033[95m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ==============================
# SAFE HELPERS
# ==============================

def set_param(world, param, value):
    try:
        world.set_weather_visual_effects_param(param=param, value=value)
    except Exception as e:
        print(RED + f"[Weather] Could not set param: {e}" + RESET)


def set_wind(drone, x, y, z):
    try:
        drone.set_external_force([x, y, z])
    except Exception as e:
        print(RED + f"[Weather] Could not set wind force: {e}" + RESET)


def reset_weather(world, drone):
    try:
        world.reset_weather_effects()
        world.enable_weather_visual_effects()
    except Exception as e:
        print(RED + f"[Weather] Could not reset weather: {e}" + RESET)

    set_param(world, WeatherParameter.RAIN,         0.0)
    set_param(world, WeatherParameter.FOG,          0.0)
    set_param(world, WeatherParameter.SNOW,         0.0)
    set_param(world, WeatherParameter.DUST,         0.0)
    set_param(world, WeatherParameter.MAPLE_LEAF,   0.0)
    set_param(world, WeatherParameter.ROAD_WETNESS, 0.0)
    set_wind(drone, 0.0, 0.0, 0.0)


# ==============================
# ENVIRONMENT FUNCTIONS
# ==============================

def clear_environment(world, drone):
    reset_weather(world, drone)
    print(GREEN + "Environment changed to CLEAR." + RESET)


def windy_environment(world, drone):
    reset_weather(world, drone)
    set_wind(drone, 10.0, 10.0, 3.0)
    print(CYAN + "Environment changed to WINDY." + RESET)


def rainy_environment(world, drone):
    reset_weather(world, drone)
    set_param(world, WeatherParameter.RAIN,         0.7)
    set_param(world, WeatherParameter.FOG,          0.2)
    set_param(world, WeatherParameter.ROAD_WETNESS, 0.8)
    set_wind(drone, 2.0, 2.0, 0.0)
    print(BLUE + "Environment changed to RAINY." + RESET)


def foggy_environment(world, drone):
    reset_weather(world, drone)
    set_param(world, WeatherParameter.FOG, 0.7)
    set_wind(drone, 1.0, 1.0, 0.0)
    print(WHITE + "Environment changed to FOGGY." + RESET)


def snowy_environment(world, drone):
    reset_weather(world, drone)
    set_param(world, WeatherParameter.FOG,          0.2)
    set_param(world, WeatherParameter.SNOW,         0.7)
    set_param(world, WeatherParameter.ROAD_WETNESS, 0.3)
    set_wind(drone, 2.0, 1.0, 0.0)
    print(CYAN + "Environment changed to SNOWY." + RESET)


def dusty_environment(world, drone):
    reset_weather(world, drone)
    set_param(world, WeatherParameter.FOG,  0.1)
    set_param(world, WeatherParameter.DUST, 0.7)
    set_wind(drone, 4.0, 2.0, 0.0)
    print(YELLOW + "Environment changed to DUSTY." + RESET)


def storm_environment(world, drone):
    reset_weather(world, drone)
    set_param(world, WeatherParameter.RAIN,         0.9)
    set_param(world, WeatherParameter.FOG,          0.5)
    set_param(world, WeatherParameter.MAPLE_LEAF,   0.4)
    set_param(world, WeatherParameter.ROAD_WETNESS, 1.0)
    set_wind(drone, 6.0, 4.0, 0.0)
    print(RED + "Environment changed to STORM." + RESET)


# ==============================
# MENU
# ==============================

def show_menu():
    print("\n" + MAGENTA + "========== PROJECT AIRSIM ENVIRONMENT SELECTOR ==========" + RESET)
    print(GREEN   + "1. Clear Environment"  + RESET)
    print(CYAN    + "2. Windy Environment"  + RESET)
    print(BLUE    + "3. Rainy Environment"  + RESET)
    print(WHITE   + "4. Foggy Environment"  + RESET)
    print(CYAN    + "5. Snowy Environment"  + RESET)
    print(YELLOW  + "6. Dusty Environment"  + RESET)
    print(RED     + "7. Storm Environment"  + RESET)
    print(MAGENTA + "8. Exit"               + RESET)
    print(MAGENTA + "==========================================================" + RESET)


# ==============================
# MAIN
# ==============================

def main():
    print("Connecting to Project AirSim...")

    client = ProjectAirSimClient()
    try:
        client.connect()
        world = World(client, "scene_basic_drone.jsonc", delay_after_load_sec=2)
        drone = Drone(client, world, "Drone1")
        drone.enable_api_control()
        drone.arm()

        print(GREEN + "Connected to Project AirSim successfully." + RESET)

        while True:
            show_menu()
            choice = input("\nEnter your choice: ")

            if choice == "1":
                clear_environment(world, drone)
            elif choice == "2":
                windy_environment(world, drone)
            elif choice == "3":
                rainy_environment(world, drone)
            elif choice == "4":
                foggy_environment(world, drone)
            elif choice == "5":
                snowy_environment(world, drone)
            elif choice == "6":
                dusty_environment(world, drone)
            elif choice == "7":
                storm_environment(world, drone)
            elif choice == "8":
                print(MAGENTA + "Exiting environment selector." + RESET)
                print(YELLOW + "Current environment will remain active in the scene." + RESET)
                break
            else:
                print(RED + "Invalid choice. Please select 1 to 8." + RESET)

        drone.disarm()
        drone.disable_api_control()

    except Exception as err:
        projectairsim_log().error(f"Exception: {err}", exc_info=True)
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()