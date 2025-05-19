import hvac

# Connect to the Vault server
client = hvac.Client(url='https://my-vault-server:8200', token='my-token')

# Write a secret to Vault
client.secrets.kv.v2.create_or_update_secret(
    path='my-secret-path',
    secret={'my-secret-key': 'my-secret-value'}
)

# Read the secret from Vault
response = client.secrets.kv.v2.read_secret_version(path='my-secret-path')
secret = response['data']['data']

# Print the secret
print(secret['my-secret-key'])
