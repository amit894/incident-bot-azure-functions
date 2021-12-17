from jira import JIRA

username="amit.894@gmail.com"
token="NotMyBitCoin"
options = {
    'server': 'https://amit894.atlassian.net/'}
jira = JIRA(
        basic_auth=(username,token),options=options)

jira.create_issue(summary="Third Issue", description="Yes this is JIRA", issuetype={'name': 'Task'}, project='MB',
                              assignee={'name': 'lakshmanchinta'})
