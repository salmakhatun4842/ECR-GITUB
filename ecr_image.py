import boto3

client = boto3.client('ecr', region_name='us-east-1')

repository_name = 'testing'

# Get list of images
images = client.describe_images(repositoryName=repository_name)['imageDetails']

# Find the latest image
latest_image = max(images, key=lambda x: x['imagePushedAt'])

# Get a list of image digests that are not the latest
non_latest_images = [image for image in images if image != latest_image]

# Delete non-latest images and prepare Markdown table
# markdown_table = "| Image Digest | Pushed At |\n|--------------|-----------|\n"
# if non_latest_images:
#     response = client.batch_delete_image(
#         repositoryName=testing,
#         imageIds=[{'imageDigest': image['imageDigest']} for image in non_latest_images]
#     )
#     for image in non_latest_images:
#         markdown_table += f"| {image['imageDigest']} | {image['imagePushedAt']} |\n"
#     print(f"Deleted {len(response['imageIds'])} images.")
# else:
#     print("No images to delete.")

# print("Markdown Table:\n")
print
