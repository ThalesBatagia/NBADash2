import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="NBA Stats Dashboard", page_icon=":basketball:", layout="wide")
st.title("Bem-vindo ao Dashboard de Estatísticas da NBA")
st.subheader("Este é um dashboard interativo para análise de estatísticas da NBA.")
st.markdown("Selecione uma das abas abaixo para visualizar as estatísticas:")


tabs = st.tabs(["Estatísticas dos times", "Estatísticas dos jogadores pelos times", "Estatísticas da carreira dos jogadores"])

def load_data():
    file_path = "NBA_Data.csv"  
    return pd.read_csv(file_path)

df = load_data()

if 'tm' not in df.columns:
    st.error("A coluna 'tm' não foi encontrada no DataFrame.")
else:
    nba_teams = {
        "MIL": "Milwaukee Bucks",
        "TOR": "Toronto Raptors",
        "DEN": "Denver Nuggets",
        "HOU": "Houston Rockets",
        "IND": "Indiana Pacers",
        "OKC": "Oklahoma City Thunder",
        "CHI": "Chicago Bulls",
        "PHI": "Philadelphia 76ers",
        "BOS": "Boston Celtics",
        "MIA": "Miami Heat",
        "SAC": "Sacramento Kings",
        "WAS": "Washington Wizards",
        "DET": "Detroit Pistons",
        "LAC": "Los Angeles Clippers",
        "GSW": "Golden State Warriors",
        "POR": "Portland Trail Blazers",
        "ORL": "Orlando Magic",
        "LAL": "Los Angeles Lakers",
        "MIN": "Minnesota Timberwolves",
        "NOP": "New Orleans Pelicans",
        "NYK": "New York Knicks",
        "BRK": "Brooklyn Nets",
        "SAS": "San Antonio Spurs",
        "ATL": "Atlanta Hawks",
        "PHO": "Phoenix Suns",
        "MEM": "Memphis Grizzlies",
        "CHO": "Charlotte Hornets",
        "DAL": "Dallas Mavericks",
        "UTA": "Utah Jazz",
        "CLE": "Cleveland Cavaliers"
        # Adicione outros times conforme necessário
    }

    df['team_name'] = df['tm'].map(nba_teams)
        


with tabs[0]:


    df['team_name'] = df['tm'].map(nba_teams)

    # Selectbox para selecionar o time
    optionn = st.selectbox(
        'Qual time você deseja visualizar?',
        df['team_name'].sort_values().unique(), key="team"
    )

    # Filtrar os dados pelo time selecionado
    filtered_df = df[df['team_name'] == optionn]

    fig1 = go.Figure(data=[go.Scatter(x=filtered_df["player"], y=filtered_df["pts_per_game"], mode='markers', name='Points per game', marker=dict(color='orange') )])
    fig1.update_layout(title=f'Pontos por jogo dos jogadores do {optionn}', xaxis_title='Jogadores', yaxis_title='Pontos por jogo')
    st.plotly_chart(fig1)

    fig2 = go.Figure(data=[go.Scatter(x=filtered_df["player"], y=filtered_df["ast_per_game"], mode='markers', name='Assists per game', marker=dict(color='purple'))])
    fig2.update_layout(title=f'Assistências por jogo dos jogadores do {optionn}', xaxis_title='Jogadores', yaxis_title='Assistências por jogo')
    st.plotly_chart(fig2)

    fig3 = go.Figure(data=[go.Scatter(x=filtered_df["player"], y=filtered_df["trb_per_game"], mode='markers', name='Rebounds per game', marker=dict(color='green'))])
    fig3.update_layout(title=f'Rebotes por jogo dos jogadores do {optionn}', xaxis_title='Jogadores', yaxis_title='Rebotes por jogo')
    st.plotly_chart(fig3)


with tabs[1]:
    
    option = st.selectbox(
        'Qual time você deseja visualizar?',
        df['team_name'].sort_values().unique(), key="team2"
    )
    filtered_df = df[df['team_name'] == option]

    option2 = st.selectbox("Qual jogador você deseja visualizar?", 
                           filtered_df['player'].sort_values().unique(), key="player")
    filtered_df2 = filtered_df[filtered_df['player'] == option2]

    fig1 = go.Figure(data=[go.Scatter(x=filtered_df2["season"], y=filtered_df2["pts_per_game"], mode='markers+lines', name='Points per game', marker=dict(color='orange') )])
    fig1.update_layout(title=f'Pontos por jogo do {option2} pela sua passagem no {option}', xaxis_title='Temporada', yaxis_title='Pontos por jogo')
    st.plotly_chart(fig1)

    fig2 = go.Figure(data=[go.Scatter(x=filtered_df2["season"], y=filtered_df2["ast_per_game"], mode='markers+lines', name='Assists per game', marker=dict(color='purple'))])
    fig2.update_layout(title=f'Assistências por jogo do {option2} pela sua passagem no {option}', xaxis_title='Temporada', yaxis_title='Assistências por jogo')
    st.plotly_chart(fig2)

    fig3 = go.Figure(data=[go.Scatter(x=filtered_df2["season"], y=filtered_df2["trb_per_game"], mode='markers+lines', name='Rebounds per game', marker=dict(color='green'))])
    fig3.update_layout(title=f'Rebotes por jogo do {option2} pela sua passagem no {option}', xaxis_title='Temporada', yaxis_title='Rebotes por jogo')
    st.plotly_chart(fig3)

with tabs[2]:
    optiono = st.selectbox(
        'Qual jogador você deseja visualizar?',
        df['player'].sort_values().unique(), key = "player2"
    )

    # Filtrar os dados pelo time selecionado
    filtered_df = df[df['player'] == optiono]
    timeplayer = filtered_df["team_name"].values

    fig1 = go.Figure(data=[go.Scatter(x=filtered_df["season"], y=filtered_df["pts_per_game"], mode='lines+markers', name='Points per game', marker=dict(color='orange'), customdata= filtered_df["team_name"].values, hovertemplate='Temporada: %{x}<br>Pontos por jogo: %{y}<br>Time: %{customdata}')])
    fig1.update_layout(title=f'Pontos por jogo do {optiono}', xaxis_title='Temporada', yaxis_title='Pontos por jogo')
    st.plotly_chart(fig1)

    fig2 = go.Figure(data=[go.Scatter(x=filtered_df["season"], y=filtered_df["ast_per_game"], mode='lines+markers', name='Assists per game', marker=dict(color='purple'), customdata= filtered_df["team_name"].values, hovertemplate='Temporada: %{x}<br>Assistências por jogo: %{y}<br>Time: %{customdata}')])
    fig2.update_layout(title=f'Assistências por jogo do {optiono}', xaxis_title='Temporada', yaxis_title='Assistências por jogo')
    st.plotly_chart(fig2)

    fig3 = go.Figure(data=[go.Scatter(x=filtered_df["season"], y=filtered_df["trb_per_game"], mode='lines+markers', name='Rebounds per game', marker=dict(color='green'), customdata= filtered_df["team_name"].values, hovertemplate='Temporada: %{x}<br>Rebotes por jogo: %{y}<br>Time: %{customdata}')])
    fig3.update_layout(title=f'Rebotes por jogo do {optiono}', xaxis_title='Temporada', yaxis_title='Rebotes por jogo')
    st.plotly_chart(fig3)
