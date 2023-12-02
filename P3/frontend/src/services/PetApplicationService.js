import { ApiService } from "./ApiService";


class PetApplicationService {
    static async get(applicationId) {
        const response = await ApiService.get(`/applications/${applicationId}`)
        return response
    }
    static async post(listingId, answers) {
        const response = await ApiService.post(`/listings/${listingId}/applications`, answers)
        return response
    }
    static async list() {
        const response = await ApiService.get(`/applications/`)
        return response
    }
}

export default PetApplicationService;