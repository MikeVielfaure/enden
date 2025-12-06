import * as Yup from 'yup';

class EventValidator {
  constructor(eventData) {
    this.event = eventData || {
      title: '',
      date: '',
      description: '',
    };
  }

  // Schéma de validation pour un événement
  getValidationSchema() {
    return Yup.object().shape({
      title: Yup.string().required('Le titre est obligatoire'),
      date: Yup.date().required('La date est obligatoire').min(new Date(), 'La date doit être dans le futur'),
      description: Yup.string().required('La description est obligatoire'),
    });
  }

  // Méthode pour valider les données de l'événement
  async validate() {
    const schema = this.getValidationSchema();
    try {
      await schema.validate(this.event, { abortEarly: false });
    } catch (validationError) {
      const errors = validationError.inner.reduce((acc, error) => {
        acc[error.path] = error.message;
        return acc;
      }, {});
      throw new Error('Validation échouée: ' + JSON.stringify(errors));
    }
  }

  
}

export default EventValidator;
