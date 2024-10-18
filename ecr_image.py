import boto3

def delete_old_ecr_images(repository_name):
    ecr_client = boto3.client('ecr')

    # Retrieve the list of images in the specified repository
    response = ecr_client.list_images(repositoryName=repository_name)

    # Get the image IDs
    image_ids = response.get('imageIds', [])

    # Create a list to hold the images that need to be deleted
    images_to_delete = []

    # Check each image to see if it is tagged with "latest"
    for image in image_ids:
        if 'imageTag' in image and image['imageTag'] != 'latest':
            images_to_delete.append(image)

    # If there are images to delete, proceed to delete them
    if images_to_delete:
        print(f"Deleting the following images from '{repository_name}':")
        for image in images_to_delete:
            print(f" - {image['imageDigest']} with tag {image['imageTag']}")
        
        delete_response = ecr_client.batch_delete_image(
            repositoryName=repository_name,
            imageIds=images_to_delete
        )
        print("Deletion response:", delete_response)
    else:
        print("No images to delete.")

if __name__ == "__main__":
    # Replace with your ECR repository name
    repository_name = 'salma'
    delete_old_ecr_images(repository_name)
