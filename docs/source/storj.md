# StorJ cloud storage (hosted on DiRAC nodes)

A quota allocation on the [StorJ cloud system](https://satellite.storj.cosma.dur.ac.uk/) is available for users who wish to share their data with selected colleagues who do not have a COSMA account.  Please ask if you would like to use this.  This can expose Object buckets via a standard S3 backend, or via a faster StorJ interface.

## StorJ usage

After logging in to the web interface, you will be presented with a project dashboard.  Within this, you can create projects (please ask if you would like your limit increasing), and within the projects, can create buckets for upload of data.  You can upload data via the web interface, or using the rclone tool.

### rclone

On a COSMA login node, first `module load rclone`.

To set a new end point (you need to do this for each bucket and project you with to interact with), use `rclone config`.  Then follow these steps:

```
n) to create a new remote
name> Give it a name (e.g. mybucket)
Select the S3 or StorJ backend (option 5 or 41 respectively at the time of writing, respectively)
```

You will then be presented with options specific for the back end.

For a S3 backend:

```
For the provider, select StorJ (option 20)
Enter your credentials (you can get this from the web interface: Access keys option in the left hand menu):
1> Enter AWS credentials
access_key_id> Copy the access key
secret_access_key> Copy the secret
endpoint> https://gateway-mt.storj.cosma.dur.ac.uk
Edit advanced config? Select n.
Yes this is OK> y
```

For the StorJ backend:

```
2> Create a new access grant  (select the API Key option within the web interface)
```

For the `satellite address>` option, copy this from the web interface, but replace `api.storj.cosma.dur.ac.uk:7777` with `storj01:7777`.

Enter the API key when prompted.

We recommend you choose a pass phrase.

And "y" to save the config.

You can then use commands such as:

- `rclone lsf mybucket:` to list a bucket
- `rclone mkdir mybucket:mydir` to make a directory
- etc

