from mission_data import mission_data
from prompts import get_system_prompt, build_user_prompt
from ai_client import analyze_mission

def run_analysis():
    print("=" * 50)
    print(f"  ARIA — ANÁLISE DE MISSÃO ESPACIAL")
    print("=" * 50)
    print(f"  Missão: {mission_data['mission_name']}")
    print(f"  Dia: {mission_data['mission_day']}")
    print(f"  Tripulação: {mission_data['crew_size']} pessoas")
    print("=" * 50)
    print("\n Conectando com ARIA...\n")

    system_prompt = get_system_prompt()
    user_prompt = build_user_prompt(mission_data)



    response = analyze_mission(system_prompt, user_prompt)

    print(response)
    print("\n" + "=" * 50)