const baseEndpoint = "/api/v1/";
const endpoints = {
    questionCRUD: `${baseEndpoint}questions/`,
    questionsAnswersList: `${baseEndpoint}questions-answers/`,
    questionsNewAnswer: `${baseEndpoint}questions-answers/`,

    answersDetail: `${baseEndpoint}answers-detail/`,
    answersLike: `${baseEndpoint}questions-like/`,

    usersDetail: `/auth/users/me`,
}

export { endpoints };