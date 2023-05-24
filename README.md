# GraphQL_Assignment
### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- GraphQL

### Installation

1. Clone the repository.
https://github.com/kashinath12345/GraphQL_Assignment.git 

2. Install the required dependencies.
Pip install -r requirements.txt

## Deployment
python manage.py runserver 

Use the Endpoint :http://localhost:8000/graphql/

# Use the following mutations to execute all the given questions in assignment.

1.question

mutation {
  createPost(
    title: "Example Title",
    description: "Example Description",
    publishDate: "2023-05-20",
    author: "Kashinath Malwade"
  ) {
    post {
      id
      title
      description
      publishDate
      author
    }
  }
}

###################################################


2.question


mutation {
  updatePost(
    id: 1
    title: "Update post Graphql"
    description: "Updated Description"
    publishDate: "2023-05-20"
    author: "Kashinath Malwade"
  ) {
    post {
      id
      title
      description
      publishDate
      author
    }
  }
}



################################################

3.question

mutation {
  createComment(
    postId: 1
    text: "I like this post and role!"
    author: "Kashinath Malwade"
  ) {
    comment {
      id
      post {
        id
        title
      }
      text
      author
    }
  }
}



################################################################

4.question 

mutation {
  deleteComment(id: "1") {
    comment {
      id
    }
  }
}


######################################

5.question 


query {
  allPosts {
    id
    title
    description
    publishDate
    author
  }
}


#######################################

6.question

query {
  post(id: "1") {
    id
    title
    description
    comments {
      id
      text
      author
    }
  }
}
