# GraphQL_Assignment

"# Blog_API_Project" 
1 st quest

mutation {
  createPost(
    title: "Example Title",
    description: "Example Description",
    publishDate: "2023-05-20",
    author: "John Doe"
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


2 question .


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

3 . ques

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

5 .question 


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

6.questions 

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