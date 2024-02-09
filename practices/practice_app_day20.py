import requests
import click

def search_github_repositories(keyword):
    url = f'https://api.github.com/search/repositories?q={keyword}'
    response = requests.get(url)
    data = response.json()
    return data['items']

@click.command()
@click.argument('keyword')
def main(keyword):
    click.echo(f"Searching GitHub repositories for '{keyword}'...")
    repositories = search_github_repositories(keyword)

    click.echo(f"Found {len(repositories)} repositories:")
    for repo in repositories:
        click.echo(f"- {repo['name']}: {repo['description']}")
        click.echo(f"  URL: {repo['html_url']}")
        click.echo(f"  Stars: {repo['stargazers_count']}")
        click.echo()

if __name__ == "__main__":
    main()